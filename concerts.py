class Concert:
    def init(self, concert_id, band_id, venue_id, date, conn):
        self.concert_id = concert_id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date
        self.conn = conn

    def band(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM bands WHERE id = %s", (self.band_id,))
            return cur.fetchone()

def venue(self):
    with self.conn.cursor() as cur:
        cur.execute("SELECT * FROM venues WHERE id = %s", (self.venue_id,))
        return cur.fetchone()

def hometown_show(self):
    with self.conn.cursor() as cur:
        cur.execute("""
            SELECT b.hometown, v.city 
            FROM bands b 
            JOIN concerts c ON b.id = c.band_id 
            JOIN venues v ON v.id = c.venue_id
            WHERE c.id = %s
        """, (self.concert_id,))
        band_hometown, venue_city = cur.fetchone()
        return band_hometown == venue_city

def introduction(self):
    with self.conn.cursor() as cur:
        cur.execute("""
            SELECT b.name, b.hometown, v.city 
            FROM bands b 
            JOIN concerts c ON b.id = c.band_id 
            JOIN venues v ON v.id = c.venue_id
            WHERE c.id = %s
        """, (self.concert_id,))
        band_name, band_hometown, venue_city = cur.fetchone()
        return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"


