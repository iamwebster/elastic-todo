uvicorn src.main:app --reload --port 8000

### elasticsearch mapping
users: 
PUT users 
{
  "settings": {
    "number_of_shards": 5,
    "number_of_replicas": 1
  },
  "mappings": {
    "properties": {
      "personal": {
        "properties": {
          "name": {"type": "text"},
          "surname": {"type": "text"},
          "age": {"type": "integer"}
        }
      },
      "contacts": {
        "properties": {
          "phone": {"type": "text"},
          "email": {"type": "text"}
        }
      },
      "created_at": {"type": "date"}
    }
  }
} 