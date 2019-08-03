(*
let () => Scanf.scanf "%d" (fun n -> Array.init n (fun ))
(fun n k x y ->
  let rest = max (n-k) 0
  let former = min n k in
  former*x + rest*y) 
  |> Printf.printf "%d\n"
*)

let () = Scanf.scanf "%d %d %d %d"
(*
let n = read_int ()
let k = read_int ()
let x = read_int ()
let y = read_int ()
*)
(fun n k x y ->
  let rest = max (n-k) 0 in
  let former = min n k in
  former*x + rest*y)
  |> Printf.printf "%d\n"
