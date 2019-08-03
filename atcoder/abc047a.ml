let () = Scanf.scanf "%d %d %d"
(fun a b c -> a+b==c || a==b+c || c+a==b)
|> (fun a -> if a then "Yes" else "No")
|> Printf.printf "%s\n"
