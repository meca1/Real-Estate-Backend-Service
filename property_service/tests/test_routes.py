# property_service/tests/test_routes.py

import unittest
from unittest.mock import patch, MagicMock
from app.routes import get_properties

class TestGetProperties(unittest.TestCase):
    
    @patch('app.routes.get_db_connection')
    def test_filter_by_year(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            {'address': '123 Main St', 'city': 'Barcelona', 'price': 250000, 'description': 'Beautiful apartment', 'status': 'for_sale'}
        ]
        
        filters = {'year': '2022'}
        properties = get_properties(filters)
        self.assertEqual(len(properties), 1)
        property_dict = properties[0].to_dict()
        self.assertEqual(property_dict['address'], '123 Main St')

    @patch('app.routes.get_db_connection')
    def test_invalid_year_filter(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = []
        
        filters = {'year': 'invalid_year'}
        properties = get_properties(filters)
        self.assertEqual(properties, [])

    @patch('app.routes.get_db_connection')
    def test_no_filters(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            {'address': '123 Main St', 'city': 'Barcelona', 'price': 250000, 'description': 'Beautiful apartment', 'status': 'for_sale'}
        ]
        
        filters = {}
        properties = get_properties(filters)
        self.assertEqual(len(properties), 1)
        property_dict = properties[0].to_dict()
        self.assertEqual(property_dict['address'], '123 Main St')

    @patch('app.routes.get_db_connection')
    def test_database_error(self, mock_get_db_connection):
        mock_get_db_connection.side_effect = Exception("Database connection error")
        
        filters = {'year': '2022'}
        with self.assertRaises(Exception):
            get_properties(filters)

if __name__ == '__main__':
    unittest.main()