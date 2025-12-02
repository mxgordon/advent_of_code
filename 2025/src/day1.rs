use anyhow::{bail, Result};

fn part1(lines: Vec<&str>) -> Result<()> {
    let mut num = 50i32;
    let max = 99;
    let mut count = 0;

    for line in lines {
        let direction = line.get(0..1).unwrap();
        let distance = line.get(1..).unwrap().parse::<i32>()?;

        match direction {
            "L" => {
                num = (num - distance) % 100;
            }
            "R" => {
                num = (num + distance) % 100;
            }
            _ => {bail!("ahhh")}
        }
        println!("{num}  {count}");
        if num == 0 {
            count += 1;
        }
    }

    println!("{}", count);

    Ok(())
}

fn part2(lines: Vec<&str>) -> Result<()> {
    let mut num = 50i64;
    let max = 99;
    let mut count = 0;

    for line in lines {
        let direction = line.get(0..1).unwrap();
        let mut distance = line.get(1..).unwrap().parse::<i64>()?;

        let was_zero = num == 0;

        count += (distance / 100).abs();
        distance = distance % 100;


        match direction {
            "L" => num -= distance,
            "R" => num += distance,
            &_ => {bail!("ahhh")}
        }

        if -100 < num && num <= 0 && !was_zero {
            count += 1;
        } else if num <= 100 {
            count += 1;
        }

        num = (num + 100) % 100;
    }

    println!("{}", count);

    Ok(())
}

pub fn run(file_data: String) -> Result<()> {
    let test_data = r#"L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"#.to_string();

    let lines = file_data
        .split(|b| b == '\n')
        .map(|line| line.strip_suffix(&['\r']).unwrap_or(line)).collect::<Vec<&str>>();

    part2(lines)?;

    Ok(())
}