from flask import Flask, request, jsonify

# Инициализация Flask приложения
app = Flask(__name__)

# Определение пути к файлу, имитирующего БД
employees_file = "employees.txt"

# Чтение данных сотрудников из файла БД. Возвраается список словарей
def read_employees_file():
    with open(employees_file, "r") as f:
        data = f.readlines()
        employees = []
        for line in data:
            id, name, email = line.strip().split(",")
            employees.append({"id": int(id), "name": name, "email": email})
        return employees

# Запись данных в файл БД
def write_employees_file(employees):
    with open(employees_file, "w") as f:
        for employee in employees:
            line = "{},{},{}\n".format(employee["id"], employee["name"], employee["email"])
            f.write(line)

# Корень API
@app.route('/', methods=['GET'])
def start_app():
    return jsonify({'status': 'Running'}), 200

# Добавление нового сотрудника в БД
@app.route('/employees', methods=['POST'])
def add_employee():
    employees = read_employees_file()
    if employees:
        id = employees[-1]["id"] + 1
    else:
        id = 1
    name = request.json['name']
    email = request.json['email']
    employee = {"id": id, "name": name, "email": email}
    employees.append(employee)
    write_employees_file(employees)
    return jsonify(employee), 201

# Получение всех сотрудников из БД
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = read_employees_file()
    return jsonify(employees), 200

# Обновление существующего сотрудника
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employees = read_employees_file()
    for employee in employees:
        if employee["id"] == id:
            employee["email"] = request.json["email"]
            write_employees_file(employees)
            return jsonify(employee), 200
    return jsonify({'error': 'Employee not found'}), 404

# Удаление сотрудника из БД
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employees = read_employees_file()
    for employee in employees:
        if employee["id"] == id:
            employees.remove(employee)
            write_employees_file(employees)
            return jsonify({'result': 'Employee deleted successfully'}), 204
    return jsonify({'error': 'Employee not found'}), 404

# Запуск Flask приложения 
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
