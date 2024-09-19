class Venue:
    def init(self, venue_id, title, city, conn):
        self.venue_id = venue_id
        self.title = title
        self.city = city
        self.conn = conn

    def concerts(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM concerts WHERE venue_id = %s", (self.venue_id,))
            return cur.fetchall()

def bands(self):
    with self.conn.cursor() as cur:
        cur.execute("""
            SELECT DISTINCT b.*
            FROM bands b
            JOIN concerts c ON b.id = c.band_id
            WHERE c.venue_id = %s
        """, (self.venue_id,))
        return cur.fetchall()

def concert_on(self, date):
    with self.conn.cursor() as cur:
        cur.execute("""
            SELECT * FROM concerts
            WHERE venue_id = %s AND date = %s
            LIMIT 1
        """, (self.venue_id, date))
        return cur.fetchone()

def most_frequent_band(self):
    with self.conn.cursor() as cur:
        cur.execute("""
            SELECT b.*, COUNT(c.id) as concert_count
            FROM bands b
            JOIN concerts c ON b.id = c.band_id
            WHERE c.venue_id = %s
            GROUP BY b.id
            ORDER BY concert_count DESC
            LIMIT 1
        """, (self.venue_id,))
        return cur.fetchone()
