-- Процедура Upsert
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phone_book WHERE contact_name = p_name) THEN
        UPDATE phone_book SET phone_number = p_phone WHERE contact_name = p_name;
    ELSE
        INSERT INTO phone_book(contact_name, phone_number) VALUES(p_name, p_phone);
    END IF;
END;
$$;

-- Процедура Bulk Insert с валидацией
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(p_names VARCHAR[], p_phones VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE
    i INTEGER;
BEGIN
    FOR i IN 1 .. array_upper(p_names, 1) LOOP
        IF length(p_phones[i]) >= 10 THEN
            INSERT INTO phone_book (contact_name, phone_number)
            VALUES (p_names[i], p_phones[i])
            ON CONFLICT (phone_number) DO NOTHING;
        END IF;
    END LOOP;
END;
$$;