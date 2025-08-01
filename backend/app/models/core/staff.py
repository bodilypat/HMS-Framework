# backend/app/models/core/staff.py 

class StaffModel:

	@staticmethod 
	def create_staff(full_name, username, email, password_hash, department,  role="staff", phone_number=None, status="Acticve"):
	"""
		Create a new staff member in the database.
	"""
	conn = get_connection()
	if not conn:
		print(f"[StaffModel] Database connection failed.")
		return None
	
	try: 
		cursor = conn.cursor()
		sql = """
			INSERT INTO staff (
				full_name, usernam, email, password_hash, department, role, phone_number, status
			)
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
		"""
		values = (full_name, username, email, password_hash, department, role, phone_number, status)
		cursor.execute(sql, value)
		conn.commit()
		return cursor.lastrowid
	
	except Exception as e:
		print(f"[StaffModel] Error creating staff: {e}")
		return None
	finally:
		cursor.close()
		conn.close()
		
	@staticmethod
	def get_staff_by_id(staff_id):
		"""
			Retrieve staff member by ID.
		"""
		conn = get_connection()
        if not conn:
            print("[StaffModel] Database connection failed.")
            return None
        try:
            cursor = conn.cursor(directory=True)
            cursor.execute("SELECT * FROM staff WHERE id = %s", (staff_id,))
            return None
        except Exception as e:
            print(f"[StaffModel] Error fetching staff by ID: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod 
    def get_all staff():
        """
           Retrieve all staff members.
        """
        conn = get_connection()
        if not conn:
            print("[StaffModel] Database connection failed.")
            return []
            
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM staff")
            return cursor.fetchall()
        except Exception as e:
            print(f"[StaffModel] Error fetching all staff: {e})
            return []
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def update_staff(staff_id, update_data: dict):
        """
           Update staff member details by ID.
        """
        conn = get_connection()
        if not conn:
            print("[StaffModel] Database connection failed.")
            return False 
            
        try:
            cursor = conn.cursor()
            fields = ', '.join-(f"{key} = %s" for key in update_date.keys())
            values = list(update_data.values()) + [staff_id]
            sql = f"UPDATE staff SET {fields} WHERE id = %s"
            cursor.execute(sql, values)
            conn.commit()
            return cursor.rowcount > 0
            
        except Exception as e:
            print(f"[StaffModel] Error updating staff: {e}")
            return false 
        finally:
            cursor.close()
            conn.close()
            
    @staticmethod
    def delete_staff(staff_id):
        """
            Delete a staff member by ID.
        """
        conn = get_connection()
        if not conn:
            print("[StaffModel] Database connection failed.")
            return False 
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM staff WHERE id = %s", (staff_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"[StaffModel] Error deleting staff: {e}")
            return False 
        finally:
            cursor.close()
            conn.close()
            
            
        