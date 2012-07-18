syn keyword pythonStatement Не Нищо Да
syn keyword pythonStatement като осигури спри продължи изтрий exec глобални
syn keyword pythonStatement ламбда нелокални карай print върни със предай
syn keyword pythonStatement клас деф nextgroup=pythonFunction skipwhite
syn keyword pythonConditional инако иначе ако
syn keyword pythonRepeat за докато
syn keyword pythonOperator и във е не или
syn keyword pythonException освен винаги вдигни опитай
syn keyword pythonInclude от внеси
syn clear pythonFunction
syn match pythonFunction "\%(\%(def\s\|деф\s\|class\s\|клас\s\|@\)\s*\)\@<=[А-Яа-яA-Za-z_]\%([А-Яа-яA-Za-z_0-9]\|\.\)*" contained
