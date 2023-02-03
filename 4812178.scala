import scala.io.StdIn
object aplusb extends App {
  for (_ <- 1 to StdIn.readInt()) {
    val Array(a, b) = StdIn.readLine().split(" ")
    println(a.toInt + b.toInt)
  }
}