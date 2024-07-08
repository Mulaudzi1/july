import streamlit as st
import requests

st.title('Service-Oriented Architecture (SOA) System')

# Function to fetch services from the backend
def get_services():
    response = requests.get('http://localhost:5000/services')
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to fetch services')
        return []

# Function to fetch a single service by ID
def get_service(service_id):
    response = requests.get(f'http://localhost:5000/service/{service_id}')
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to fetch service')
        return None

# Display all services
st.header('Available Services')
services = get_services()
for service in services:
    st.subheader(service['name'])
    st.write(service['description'])

# Input for service ID to fetch details
service_id = st.number_input('Enter service ID to fetch details', min_value=1)
if st.button('Get Service Details'):
    service = get_service(service_id)
    if service:
        st.subheader(service['name'])
        st.write(service['description'])
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data (this can be replaced with a database connection)
services = [
    {"id": 1, "name": "Service 1", "description": "This is service 1"},
    {"id": 2, "name": "Service 2", "description": "This is service 2"},
]

@app.route('/services', methods=['GET'])
def get_services():
    return jsonify(services)

@app.route('/service/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = next((s for s in services if s['id'] == service_id), None)
    if service:
        return jsonify(service)
    else:
        return jsonify({'message': 'Service not found'}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)

