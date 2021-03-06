
from datetime import date
from mock import Mock
import os.path
import csv
from scraper.raw_inmate_data import RawInmateData, RAW_INMATE_DATA_BUILD_DIR, RAW_INMATE_DATA_RELEASE_DIR, \
    STORE_RAW_INMATE_DATA, FEATURE_CONTROL_IDS


class TestRawInmateData:

    def __add_inmates(self, feature_activated=True):
        feature_controls = self.__feature_controls(feature_activated)
        raw_inmate_data = RawInmateData(self.__today, feature_controls, Mock())
        raw_inmate_data.add(self.__inmates.next())
        raw_inmate_data.add(self.__inmates.next())
        return raw_inmate_data

    def __assert_build_file(self, raw_inmate_data):
        # noinspection PyProtectedMember
        raw_inmate_data._RawInmateData__build_file.flush()
        build_dir_list = self.__build_dir.listdir()
        self.__assert_one_build_file(build_dir_list)
        with open(str(build_dir_list[0]), 'rb') as csvfile:
            build_file_reader = csv.reader(csvfile)
            header = build_file_reader.next()
            self.__assert_header(header)
            self.__inmates.prep_check_created_inmates()
            for inmate_info in build_file_reader:
                self.__inmates.check_inmate(inmate_info)

    def __assert_header(self, header):
        expected = ['Booking_Id', 'Booking_Date', 'Inmate_Hash', 'Gender', 'Race', 'Height', 'Weight',
                    'Age_At_Booking', 'Housing_Location', 'Charges', 'Bail_Amount', 'Court_Date', 'Court_Location']
        assert header == expected

    def __assert_one_build_file(self, build_dir_list):
        assert len(build_dir_list) == 1
        filename = os.path.basename(str(build_dir_list[0]))
        assert filename == self.__today.strftime('%Y-%m-%d.csv')

    def __assert_release_file(self):
        release_dir_list = self.__raw_inmate_data_dir.listdir()
        self.__assert_year_dir(release_dir_list)
        released_file_name = os.path.join(os.path.join(str(self.__raw_inmate_data_dir), self.__today.strftime('%Y')),
                                          self.__today.strftime('%Y-%m-%d.csv'))
        assert os.path.exists(released_file_name)
        with open(released_file_name, 'r') as csvfile:
            raw_inmate_data_reader = csv.reader(csvfile)
            header = raw_inmate_data_reader.next()
            self.__assert_header(header)
            self.__inmates.prep_check_created_inmates()
            for inmate_info in raw_inmate_data_reader:
                self.__inmates.check_inmate(inmate_info)

    def __assert_year_dir(self, dir_list):
        assert len(dir_list) == 1
        dir_name = os.path.basename(str(dir_list[0]))
        assert dir_name == self.__today.strftime('%Y')

    def __feature_controls(self, feature_activated):
        feature_controls = {
            RAW_INMATE_DATA_BUILD_DIR: str(self.__build_dir),
            RAW_INMATE_DATA_RELEASE_DIR: str(self.__raw_inmate_data_dir),
            STORE_RAW_INMATE_DATA: feature_activated
        }
        return feature_controls

    def __make_tmp_dirs(self, tmp_dir):
        self.__raw_inmate_data_dir = tmp_dir.mkdir("raw_inmate_data")
        self.__build_dir = tmp_dir.mkdir("build_dir")

    def setup_method(self, method):
        self.__today = date.today()
        self.__inmates = Inmates(self.__today)

    def test_adding_inmates_populates_build_file(self, tmpdir):
        self.__make_tmp_dirs(tmpdir)
        raw_inmate_data = self.__add_inmates()
        assert len(self.__raw_inmate_data_dir.listdir()) == 0
        self.__assert_build_file(raw_inmate_data)

    def test_feature_switch_off_means_no_processing(self, tmpdir):
        self.__make_tmp_dirs(tmpdir)
        raw_inmate_data = self.__add_inmates(feature_activated=False)
        raw_inmate_data.finish()
        assert len(self.__raw_inmate_data_dir.listdir()) == 0
        assert len(self.__build_dir.listdir()) == 0

    def test_no_feature_controls(self, tmpdir):
        self.__make_tmp_dirs(tmpdir)
        raw_inmate_data = RawInmateData(self.__today, None, Mock())
        raw_inmate_data.add(self.__inmates.next())
        raw_inmate_data.finish()
        assert len(self.__raw_inmate_data_dir.listdir()) == 0
        assert len(self.__build_dir.listdir()) == 0

    def test_no_feature_controls(self, tmpdir):
        self.__make_tmp_dirs(tmpdir)
        raw_inmate_data = RawInmateData(self.__today, None, Mock())
        raw_inmate_data.add(self.__inmates.next())
        raw_inmate_data.finish()
        assert len(self.__raw_inmate_data_dir.listdir()) == 0
        assert len(self.__build_dir.listdir()) == 0

    def test_feature_active_no_dirs(self, tmpdir):
        self.__make_tmp_dirs(tmpdir)
        for feature_control in FEATURE_CONTROL_IDS:
            feature_controls = self.__feature_controls(feature_activated=True)
            del feature_controls[feature_control]
            raw_inmate_data = RawInmateData(self.__today, feature_controls, Mock())
            raw_inmate_data.add(self.__inmates.next())
            raw_inmate_data.finish()
            assert len(self.__raw_inmate_data_dir.listdir()) == 0
            assert len(self.__build_dir.listdir()) == 0

    def test_finishing_places_inmates_file_in_public_dir(self, tmpdir):
        self.__make_tmp_dirs(tmpdir)
        raw_inmate_data = self.__add_inmates()
        raw_inmate_data.finish()
        assert len(self.__build_dir.listdir()) == 0
        self.__assert_release_file()

    def test_initialize(self, tmpdir):
        self.__make_tmp_dirs(tmpdir)
        feature_controls = self.__feature_controls(feature_activated=True)
        RawInmateData(self.__today, feature_controls, Mock())
        assert len(self.__raw_inmate_data_dir.listdir()) == 0
        assert len(self.__build_dir.listdir()) == 0


class Inmates:

    INMATE_DETAILS_METHOD_NAMES = ['jail_id', 'booking_date', 'hash_id', 'gender', 'race', 'height', 'weight',
                                   'age_at_booking', 'housing_location', 'charges', 'bail_amount', 'next_court_date',
                                   'court_house_location']

    def __init__(self, today):
        self.__id = 0
        self.__cur_booking_date = today.strftime('%Y-%m-%d')
        self.__jail_id_template = today.strftime("%Y-%m%d%%03d")
        self.__created_inmates_index = 0
        self.__created_inmates = []

    def __age_at_booking(self):
        return '21'

    def __bail_amount(self):
        return 'NO BAIL'

    def __booking_date(self):
        return self.__cur_booking_date

    def __charges(self):
        return '506(23)'

    def check_inmate(self, inmate):
        assert self.__created_inmates_index < len(self.__created_inmates)
        expected = self.__convert_inmate_to_array(self.__created_inmates[self.__created_inmates_index])
        assert inmate == expected
        self.__created_inmates_index += 1

    @staticmethod
    def __convert_inmate_to_array(inmate_details):
        return [getattr(inmate_details, method_name)() for method_name in Inmates.INMATE_DETAILS_METHOD_NAMES]

    def __court_house_location(self):
        return 'Count 101'

    def __gender(self):
        return 'M'

    def __hash_id(self):
        return '26'

    def __height(self):
        return '511'

    def __housing_location(self):
        return '01-01'

    def __jail_id(self):
        self.__id += 1
        return self.__jail_id_template % self.__id

    def next(self):
        inmate = Mock()
        for method_name in Inmates.INMATE_DETAILS_METHOD_NAMES:
            new_method = Mock()
            new_method.return_value = getattr(self, '_Inmates__%s' % method_name)()
            inmate.attach_mock(new_method, method_name)
        self.__created_inmates.append(inmate)
        return inmate

    def __next_court_date(self):
        return '2525-01-01'

    def prep_check_created_inmates(self):
        self.__created_inmates_index = 0

    def __race(self):
        return 'WH'

    def __weight(self):
        return '188'
