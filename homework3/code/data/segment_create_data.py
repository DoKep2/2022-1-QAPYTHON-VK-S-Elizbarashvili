from homework3.input_data_generator import MyFaker


class SegmentCreateData:

    data = {
        "name": MyFaker.fake_name(),
        "logicType": "or",
        "pass_condition": "1",
        "relations": [
            {
                "object_type": "remarketing_player",
                "params": {
                    "type": "positive",
                    "left": "365",
                    "right": "0"
                },
            }
        ]
    }