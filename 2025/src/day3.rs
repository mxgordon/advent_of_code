use anyhow::{bail, Result};

fn part1(lines: Vec<&str>) -> Result<()> {
    let mut total_joltage = 0;

    for batteries in lines {
        let batteries = batteries.chars().map(|c| c.to_digit(10).unwrap()).collect::<Vec<u32>>();

        let max_battery = batteries[..batteries.len()-1].iter().max().unwrap();
        let max_batt_idx = batteries.iter().position(|b| b==max_battery).unwrap();

        let next_battery = batteries[max_batt_idx+1..].iter().max().unwrap();

        total_joltage += max_battery * 10 + next_battery;
    }

    println!("{total_joltage}");

    Ok(())
}

fn part2(lines: Vec<&str>) -> Result<()> {
    let mut total_joltage = 0u64;

    let b_cnt = 12;

    for batteries in lines {
        let batteries = batteries.chars().map(|c| c.to_digit(10).unwrap()).collect::<Vec<u32>>();

        let mut last_idx = 0;

        for batt_num in (0..b_cnt).rev() {
            let max_idx = batteries.len() - batt_num;
            let max_battery = batteries[last_idx..max_idx].iter().max().unwrap();
            let max_batt_idx = batteries[last_idx..max_idx].iter().position(|b| b==max_battery).unwrap() + last_idx;
            last_idx = max_batt_idx + 1;

            total_joltage += (*max_battery as u64) * 10u64.pow(batt_num as u32);
        }
    }

    println!("{total_joltage}");

    Ok(())
}

pub fn run(file_data: String) -> Result<()> {
    let test_data = r#"987654321111111
811111111111119
234234234234278
818181911112111"#.to_string();

    let lines = file_data
        .split(|b| b == '\n')
        .map(|line| line.strip_suffix(&['\r']).unwrap_or(line)).collect::<Vec<&str>>();

    part2(lines)?;

    Ok(())
}