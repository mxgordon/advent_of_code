extern crate core;

use std::fs::read_to_string;

mod day1;

macro_rules! day_run {
    ($dayn:tt) => {
        $dayn::run(read_file(stringify!($dayn))?)?

    };
}


fn read_file(day: &str) -> anyhow::Result<String> {
    Ok(read_to_string(format!("data/{day}.txt"))?)
}


fn main() -> anyhow::Result<()> {
    day_run!(day1);

    Ok(())
}
