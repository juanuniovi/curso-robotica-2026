======
# Guía rápida de Git

## 1. Configuración inicial

```bash
git config --global user.name "Tu nombre"
git config --global user.email "tu@email.com"
```

## 2. Crear o descargar un repositorio

```bash
# Crear un repositorio en la carpeta actual
git init

# Descargar un repositorio remoto
git clone <URL_DEL_REPOSITORIO>
```

## 3. Consultar el estado y el historial

```bash
git status                 # Ver cambios pendientes
git log --oneline          # Ver el historial resumido
git diff                   # Ver cambios aún no preparados
```

## 4. Guardar cambios: add y commit

```bash
git add archivo.txt        # Preparar un archivo
git add .                  # Preparar todos los cambios
git commit -m "Describe el cambio"  # Crear un commit
```

Un commit guarda una versión local de los cambios. Conviene usar mensajes breves y descriptivos.

## 5. Ramas

```bash
git branch                  # Listar ramas
git switch -c nueva-rama    # Crear y cambiar a una rama
git switch main             # Cambiar de rama
git branch -d nueva-rama    # Eliminar una rama local
```

## 6. Sincronizar con el repositorio remoto

```bash
git remote -v                         # Ver repositorios remotos
git pull origin main                  # Descargar e integrar cambios
git push origin main                  # Subir commits
git push -u origin nueva-rama         # Publicar una rama por primera vez
```

`git pull` equivale normalmente a descargar cambios (`fetch`) e integrarlos. Antes de hacer `push`, conviene ejecutar `pull` para reducir conflictos.

## 7. Resolver conflictos

Si `git pull` produce conflictos:

```bash
git status                 # Ver archivos en conflicto
```

Edita esos archivos, elimina las marcas `<<<<<<<`, `=======` y `>>>>>>>`, y después ejecuta:

```bash
git add <archivo-resuelto>
git commit -m "Resolver conflictos"
git push origin main
```

## 8. Deshacer cambios

```bash
git restore archivo.txt            # Descartar cambios no guardados
git restore --staged archivo.txt   # Quitar un archivo del staging
git revert <ID_DEL_COMMIT>         # Crear un commit que deshace otro
```

> Evita `git reset --hard` si no estás seguro: puede eliminar cambios definitivamente.
>>>>>>> 29668d5d093a9d0b3388b483769d1c8e839dbce3
