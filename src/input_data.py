def define_input_data():
    input_data = {
        "Historische Aktienpreise": [
            "Eröffnungskurs",
            "Schlusskurs",
            "Höchstkurs",
            "Tiefstkurs"
        ],
        "Handelsvolumen": "Volumen der gehandelten Aktien",
        "Wirtschaftsindikatoren": [
            "S&P 500 Index",
            "Inflationsrate",
            "Zinssätze"
        ]
    }
    return input_data

if __name__ == "__main__":
    data_definitions = define_input_data()
    for data_type, details in data_definitions.items():
        print(f"{data_type}: {details}")