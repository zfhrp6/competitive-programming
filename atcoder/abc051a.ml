let () =
Scanf.scanf "%s"
(fun s -> String.concat " " [String.sub s 0 5; String.sub s 6 7; String.sub s 14 5])
|> Printf.printf "%s\n"
