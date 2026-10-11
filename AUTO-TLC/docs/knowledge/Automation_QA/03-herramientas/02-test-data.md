# Test Data Management

> **Archivo:** 2 de 3 | **Sección:** Herramientas | **Nivel:** Intermedio

---

## Definición

La **gestión de datos de prueba** organiza, crea y mantiene datos utilizados en tests automatizados.

## Estrategias

| Estrategia | Descripción | Cuándo usar |
|------------|-------------|-------------|
| **Data Factory** | Generar datos programáticamente | Tests repetitivos |
| **Fixture Files** | Datos en archivos JSON/CSV | Datos estáticos |
| **Database Seeds** | Poblar BD antes de tests | Datos complejos |
| **API Setup** | Crear vía API antes de test | Datos dinámicos |

## Data Factory

### Java

```java
public class UserFactory {
    public static User createRandom() {
        User user = new User();
        user.setName("User_" + System.currentTimeMillis());
        user.setEmail("user" + System.currentTimeMillis() + "@test.com");
        user.setPassword("Password123!");
        return user;
    }
}
```

### Python

```python
class UserFactory:
    @staticmethod
    def create_random():
        return {
            'name': f'User_{uuid.uuid4().hex[:8]}',
            'email': f'user_{uuid.uuid4().hex[:8]}@test.com',
            'password': 'Password123!'
        }
```

## Fixture Files

### users.json

```json
{
  "validUser": {
    "email": "user@test.com",
    "password": "Password123!"
  },
  "invalidUser": {
    "email": "invalid@test.com",
    "password": "wrong"
  }
}
```

### Uso en Cypress

```javascript
cy.fixture('users.json').then((users) => {
  cy.login(users.validUser.email, users.validUser.password);
});
```

## Resumen

- **Gestión de datos** es crítica para tests repetibles
- **Data Factory** para datos dinámicos
- **Fixtures** para datos estáticos
- **API Setup** para datos complejos

---

## Navegación

- **Anterior:** [01-page-objects.md](01-page-objects.md)
- **Siguiente:** [03-reporting.md](03-reporting.md)
- **Volver a Herramientas:** [README.md](README.md)
- **Volver al índice:** [MASTER-README.md](../MASTER-README.md)

---

*Archivo 2 - Test Data Management*
