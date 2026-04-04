-- Функция поиска по шаблону
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p_pattern TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT contact_name, phone_number FROM phone_book
    WHERE contact_name ILIKE '%' || p_pattern || '%' 
       OR phone_number ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Функция для пагинации
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INTEGER, p_offset INTEGER)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT contact_name, phone_number FROM phone_book
    ORDER BY contact_name
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;