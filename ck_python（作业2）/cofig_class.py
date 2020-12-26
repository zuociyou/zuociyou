import yaml
class Test_config():
    def get_data(self):
        # with open("datas.yml", encoding='utf-8') as f:
        with open("datas.yml") as f:
            datas = yaml.safe_load(f)
            # print(datas)
            add_data = datas["add_data"]
            sub_data = datas["sub_data"]
            mun_data = datas["mun_data"]
            div_data = datas["div_data"]
            myids = datas["myids"]
            return [add_data, sub_data, myids, mun_data, div_data]