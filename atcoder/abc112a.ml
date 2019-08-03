let f a = match a with
1 -> "Hello World"
| _ -> Scanf.scanf "%d %d" (fun a b -> string_of_int (a+b));;
Scanf.scanf "%d" f
|> Printf.printf "%s\n"
