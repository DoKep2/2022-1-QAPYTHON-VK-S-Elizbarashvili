from util.data_generator import DataGenerator


class Test:
    def test_get_teacher(self, mock_client, name=DataGenerator.fake_name()):
        surname = mock_client.get_teacher_rate(name)
        assert 'not found' in surname

    def test_add_teacher(self, mock_client, name=DataGenerator.fake_name(), rate=DataGenerator.fake_number()):
        mock_client.add_teacher_rate(name, rate)
        a = mock_client.get_teacher_rate(name)
        assert str(a) == rate

    def test_delete_teacher_rate(self, mock_client, name=DataGenerator.fake_name(), rate=DataGenerator.fake_number()):
        mock_client.add_teacher_rate(name, rate)
        mock_client.delete_teacher_rate(name)
        a = mock_client.get_teacher_rate(name)
        assert 'not found' in a

    def test_update_teacher_rate(self, mock_client, name=DataGenerator.fake_name(), rate=DataGenerator.fake_number(),
                                 new_rate=DataGenerator.fake_number()):
        mock_client.add_teacher_rate(name, rate)
        mock_client.update_teacher_rate(name, new_rate)
        a = mock_client.get_teacher_rate(name)
        assert str(a) == new_rate
