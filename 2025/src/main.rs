extern crate core;

use std::fs::read_to_string;

mod day1;
mod day2;

macro_rules! day_run {
    ($day_n:tt) => {
        $day_n::run(read_file(stringify!($day_n))?)?

    };
}


fn read_file(day: &str) -> anyhow::Result<String> {
    Ok(read_to_string(format!("data/{day}.txt"))?)
}


fn main() -> anyhow::Result<()> {
    day_run!(day2);

    Ok(())
}
