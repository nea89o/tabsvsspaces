name tabsvsspaces
user romangraef
ver 1.0.0

func install {
	mkdir -p /usr/share/tabsvsspaces
	cp -rf * /usr/share/tabsvsspaces
	ln -fs /usr/share/tabsvsspaces/main.py /usr/bin/tabsvsspaces
}

func update {
    &install
}

func install_win {
    &werror
}

func update_win
{
    &install_win
}

func remove_win {
    &werror
}

func werror {
    @echo "Leider gibt es keinen Windows-Support."
}

