let calc = fun a b c -> String.concat "" (List.map (fun s -> String.make 1 s.[0]) [a;b;c])
let () = Scanf.scanf "%s %s %s"
(fun atcoder hoge contest -> calc atcoder hoge contest)
|> Printf.printf "%s\n"
