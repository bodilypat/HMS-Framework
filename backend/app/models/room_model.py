from backend.config.dbconnect import get_connection 

class RoomModel:
	@staticmethod
	def create_room(room_number, room_tpe_id, floor_number, price_per_night, room_status='Available',
	                room_description=None, beds_count=1, capacity=1):
		"""Insert a new room into the database."""
		conn = get_connection()
		if not conn:
			return None
		try:
			cursor = conn.cursor()
			sql = """
				INSERT INTO rooms (
					room_number, room_type_id, floor_number, price_per_night,
					room_status, room_description, beds_count, capacity
				)
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
			"""
			values = (
				room_number, room_type_id, floor_number, price_per_night, room_status, room_description,
				beds_count, capacity
			)
			cursor.execute(sql, values)
			conn.commit()
			return cursor.lastwid
		except Exception as e:
			print(f" Error creating room: {e}")
			return None
		finally:
			cursor.close()
			conn.close()
			
		@staticmethod
		def get_room_by_id(room_id):
            """Retrieve room details by room ID."""
            conn = get_connection()
            if not conn:
                return None 
            try:
                cursor = conn.cursor(dictionary=True) 
                cursor.execute("SELECT * FROM rooms WHERE room_id = %s", (room_id,))
                return cursor.fetchone()
            except Exception as e:
                print(f" Error fetching room: {e}")
                return None 
            finally:
                cursor.close()
                conn.close()
                
        @staticmethod 
        def get_all_rooms():
            """Retrieve all rooms"""
            conn = get_connection() 
            if not conn 
                return []
            try:
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM rooms")
                return cursor.fetchall()
            except Exception as e:
                print(f" Error fetching rooms: {e}")
                return []
            finally:
                cursor.close()
                conn.close()
                
       @staticmethod 
       def update_room_status(room_id, new_status):
           """Update the status to a room (Available, Occupied, Maintenance). """
           conn = get_connection()
           if not conn:
              return False
              
           try:
              cursor = conn.cursor() 
              sql = "UPDATE rooms SET room_status = %s WHERE room_id = %s"
              cursor.execute(sql, (new_status, room_id))
              conn.commit()
              return cursor.rowcount > 0
           except Exception as e:
              print(f "Error updating room status: {e}")
              return False 
           finally:
              cursor.close() 
              conn.close()
              
      @staticmethod 
      def delete_room(room_id):
         """Delete a room by its ID."""
         conn = get_connect() 
         if not conn:
            return False
            
         try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM rooms WHERE room_id = %s", (room_id,)) 
            conn.commit()
            return cursor.rowcount > 0
         except Exception as e:
            print(f" Error deleting room: {e}")
            return False
         finally:
            cursor.close()
            conn.close() 
            
            
		