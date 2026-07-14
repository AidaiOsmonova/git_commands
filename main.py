# git - система контроля версий (версий кода)

# github/gitlab/bitbucket - хранилище/сайт для хранения (версий) кода

# repository/репозиторий - папка в которой git отслеживает изменения

# git init - создание репозитория

# git status - проверка статуса отслеживания 

# git add <file_name> or . - добавление файла в список отслеживания (в staging area)

# git commit -m 'some message' - фиксация\создание версии кода с сообщением

# git commit -am 'some message' - добавление существующего файла в список отслеживания
# и фиксация/ создание версии кода с сообщением

# git remote add <variable name>(обычно название origin) <link to repository>
# связка локального репозитория с удаленным и сохранение ссылки в переменную

# git push origin <branch_name> -  отправкв версии кода в удаленный репозиторий

# ветка/branch - копия кода независимая от основной версии кода.

# git branch - вывод списка веток
# git branch <new_branch_name> -  создание новой ветки
# git checkout <branch name> - переход на указанную ветку
# git checkout -b <new_branch_name> -  создание новой веки и сразу переход в нее

# git megre <branch name> - склеивание указанной ветки в текущую

# git pull origin <branch_name> - стягивание/добавление изменений с указаннй ветки в текущую

# git clone <link_to_repository> - скачивание/клонирование указанного репозитория 
