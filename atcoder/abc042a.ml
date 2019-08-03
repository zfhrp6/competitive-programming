let () = Scanf.scanf "%d %d %d"
(fun a b c -> (a==5&&b==5&&c==7)||(a==5&&b==7&&c==5)||(a==7&&b==5&&c==5))
|> (fun b -> if b then "YES" else "NO")
|> Printf.printf "%s\n"
