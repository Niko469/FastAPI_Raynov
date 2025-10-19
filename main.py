from fastapi import FastAPI

app = FastAPI()

# Llista d'usuaris d'exemple
users = [
    {"id": 1, "nom": "Nikolay", "edat": 18},
    {"id": 2, "nom": "Hunain", "edat": 19},
    {"id": 3, "nom": "Ibai", "edat": 20},
    {"id": 4, "nom": "Ronaldo", "edat": 40}
]

# CREATE
@app.post("/api/users")
async def add_user(id: int, nom: str, edat: int):
    nou_usuari = {"id": id, "nom": nom, "edat": edat}
    users.append(nou_usuari)
    return {"usuaris": users}

# READ - all
@app.get("/api/users")
async def get_all_users():
    return {"total": len(users), "usuaris": users}

# READ - id
@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    for i in users:
        if i["id"] == user_id:
            return {"usuari_trobat": i}
    return {"error": "No s'ha trobat cap usuari amb aquest id"}

# UPDATE
@app.put("/api/users/{user_id}")
async def update_user(user_id: int, nom: str, edat: int):
    for i in users:
        if i["id"] == user_id:
            i["nom"] = nom
            i["edat"] = edat
            return {"usuaris": users}
        return {"error": "Usuari no existeix"}

# DELETE
@app.delete("/api/users/{users_id}")
async def delete_user(user_id: int):
    for i in users:
        if i["id"] == user_id:
            users.remove(i)
            return{"restants": users}
        return {"error": "Usuari no trobat"}