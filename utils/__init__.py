def zip_rows(rows):
    return [dict(zip(row.keys(), row)) for row in rows]
