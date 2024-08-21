from app.database import get_db_connection
from app.models import PropertyResponse, format_properties
from typing import Dict, List

def build_query(filters: Dict[str, str]) -> str:
    """
    Builds the SQL query based on the provided filters.
    """
    query = """
    SELECT p.address, p.city, p.price, p.description, s.name AS status
    FROM property p
    JOIN (
        SELECT sh.property_id, s.name
        FROM status_history sh
        JOIN status s ON sh.status_id = s.id
        WHERE sh.id = (
            SELECT MAX(sh_inner.id)
            FROM status_history sh_inner
            WHERE sh_inner.property_id = sh.property_id
        )
    ) s ON p.id = s.property_id
    WHERE 1=1
    """
    
    if filters.get('year'):
        query += " AND p.year = %s"
    if filters.get('city'):
        query += " AND p.city = %s"
    if filters.get('status'):
        query += " AND s.name = %s"
    
    return query

def get_query_params(filters: Dict[str, str]) -> List[str]:
    """
    Extracts the parameters from the filters dictionary.
    """
    params = []
    if filters.get('year'):
        params.append(filters['year'])
    if filters.get('city'):
        params.append(filters['city'])
    if filters.get('status'):
        params.append(filters['status'])
    
    return params

def execute_query(query: str, params: List[str]) -> List[Dict]:
    """
    Executes the SQL query and returns the results.
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    properties = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return properties

def get_properties(filters: Dict[str, str]) -> List[PropertyResponse]:
    """
    Retrieves properties based on filters and formats the response.
    """
    query = build_query(filters)
    params = get_query_params(filters)
    properties = execute_query(query, params)
    return format_properties(properties)