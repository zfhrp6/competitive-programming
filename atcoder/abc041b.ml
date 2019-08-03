let rec iexp acc a b = if b=0 then acc else iexp (acc*a) a (b-1);;
let exp a b = iexp 1 a b;;
let m a = (mod) a (7 + (exp 10 9));;
let f a b c = m ((m a)*(m b)*(m c));;
let () = Scanf.scanf "%d %d %d" f
|> Printf.printf "%d\n"
