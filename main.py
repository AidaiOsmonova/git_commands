# git - система контроля версий (версий кода)

# github/gitlab/bitbucket - хранилище/сайт для хранения (версий) кода

# repository/репозиторий - папка в которой git отслеживает изменения

# git init - создание репозитория

# git status - проверка статуса отслеживания 

# git add <file_name> or . - добавление файла в список отслеживания (в staging area)

# git commit -m 'some message' - фиксация\создание версии кода с сообщением

# git remote add <variable name>(обычно название origin) <link to repository>
# связка локального репозитрия с удаленным и сохранение ссылки в переменную

# git push origin <branch_name> -  отправкв версии кода в удаленный репозиторий

# ветка/branch - копия кода независимая от основной версии кода.

# git branch - вывод списка веток
# git branch <new_branch_name> -  создание новой ветки
# git checkout <branch name> - переход на указанную ветку


# git checkout -b <new_branch_name> - создание новой ветки и переход на указанную ветку
# git merge <branch_name> - склеивание веток. Склеивает указанную ветку к текущей(на которой находитесь)