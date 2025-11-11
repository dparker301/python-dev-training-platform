from app import app
def test_health():
    with app.test_client() as c:
        rv = c.get('/api/health')
        assert rv.status_code == 200
        assert rv.get_json()['status'] == 'ok'
