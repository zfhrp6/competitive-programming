module IntSet = Set.Make(struct type t = int let compare x y = x-y end)
let () = Scanf.scanf "%d %d %d"
(fun a b c -> let s = List.fold_right IntSet.add [a;b;c] IntSet.empty in IntSet.cardinal s)
|> Printf.printf "%d\n"
