let rec f s = if String.length s=0 then 0 else f (String.sub s 1 (String.length s-1)) + if s.[0]='1' then 1 else 0;;
Scanf.scanf "%s" f
|> Printf.printf "%d\n"
