class Band:
    def init(self, band_id, name, hometown, conn):
        self.band_id = band_id
        self.name = name
        self.hometown = hometown
        self.conn = conn

    def concerts(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM concerts WHERE band_id = %s", (self.band_id,))
            return cur.fetchall()

def venues(self):
    with self.conn.cursor() as cur:
        cur.execute("""
            SELECT DISTINCT v.*
            FROM venues v
            JOIN concerts c ON v.id = c.venue_id
            WHERE c.band_id = %s
        """, (self.band_id,))
        return cur.fetchall()

def play_in_venue(self, venue, date):
    with self.conn.cursor() as cur:
        # Check if the venue exists in the database
        cur.execute("SELECT id FROM venues WHERE title = %s", (venue,))
        venue_record = cur.fetchone()

        if venue_record is None:
            raise ValueError(f"Venue '{venue}' not found in the database.")

        venue_id = venue_record[0]
        cur.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (%s, %s, %s)", (self.band_id, venue_id, date))
        self.conn.commit()

def all_introductions(self):
    with self.conn.cursor() as cur:
        cur.execute("""
            SELECT v.city, b.name, b.hometown
            FROM concerts c
            JOIN bands b ON b.id = c.band_id
            JOIN venues v ON v.id = c.venue_id
            WHERE b.id = %s
        """, (self.band_id,))
        concerts = cur.fetchall()
        return [f"Hello {city}!!!!! We are {self.name} and we're from {self.hometown}" for city, _, _ in concerts]

@staticmethod
def most_performances(conn):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT b.*, COUNT(c.id) as concert_count
            FROM bands b
            JOIN concerts c ON b.id = c.band_id
            GROUP BY b.id
            ORDER BY concert_count DESC
            LIMIT 1
        """)
        return cur.fetchone()