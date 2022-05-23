from util.data_generator import DataGenerator


class Test:
    def test_get_non_existent_teacher(self, mock_client, name=DataGenerator.fake_name()):
        rate = mock_client.get_teacher_rate(name)
        assert 'not found' in rate

    def test_add_teacher(self, mock_client, name=DataGenerator.fake_name(), rate=DataGenerator.fake_number()):
        mock_client.add_teacher_rate(name, rate)
        teacher_rate = mock_client.get_teacher_rate(name)
        assert teacher_rate == rate

    def test_delete_teacher_rate(self, mock_client, name=DataGenerator.fake_name(), rate=DataGenerator.fake_number()):
        mock_client.add_teacher_rate(name, rate)
        mock_client.delete_teacher_rate(name)
        teacher_rate = mock_client.get_teacher_rate(name)
        assert 'not found' in teacher_rate

    def test_update_teacher_rate(self, mock_client, name=DataGenerator.fake_name(), rate=DataGenerator.fake_number(),
                                 new_rate=DataGenerator.fake_number()):
        mock_client.add_teacher_rate(name, rate)
        mock_client.update_teacher_rate(name, new_rate)
        rate = mock_client.get_teacher_rate(name)
        assert rate == new_rate
