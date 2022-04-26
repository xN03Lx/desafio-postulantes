from client import RequestsClient
from services import ServiceSii
from utils import save_data_as_json_file


def main():
    client = RequestsClient()
    service = ServiceSii(client=client)

    url_request = 'servicios_online/1047-nomina_inst_financieras-1714.html'
    data_nomina = service.get_data_nomina(url_request)

    file_name = url_request.split('/')[1].replace('.html', "")
    save_data_as_json_file(file_name, data_nomina)

    print(f'Saved json file ./{file_name}.json')

if __name__ == "__main__":
    main()
