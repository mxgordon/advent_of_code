use anyhow::{bail, Result};

fn part2(lines: Vec<&str>) -> Result<()> {
    let mut score = 0i64;

    for line in lines {
        let (str1, str2) = line.split_once('-').unwrap();

        let num1 = str1.parse::<i64>()?;
        let num2 = str2.parse::<i64>()?;

        for num in num1..(num2 + 1) {
            let num_str = num.to_string();
            let num_str_len = num_str.len();
            let sub_num_str_len = (num_str_len + 1) / 2;

            if num_str_len  == 1 {
                continue;
            }

            // println!("Trying {num}");

            'factor_check: for num_sz in 1..(sub_num_str_len + 1) {
                let num_count = num_str_len / num_sz;

                if num_count * num_sz == num_str_len {
                    // println!("Factors: size: {num_sz}  count: {num_count}  -  {num_str_len}");
                    let test_sub_num_str = &num_str[..num_sz];

                    for section_num in 1..num_count {
                        let section_str = &num_str[(section_num * num_sz)..((section_num + 1) * num_sz)];

                        if section_str != test_sub_num_str {
                            continue 'factor_check;
                        }
                    }

                    score += num;
                    println!("Found {num}");
                    break 'factor_check;
                }
            }
        }
    }

    println!("{score}");

    Ok(())
}

pub fn run(file_data: String) -> Result<()> {
    let test_data = r#"11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"#.to_string();

    let lines = file_data
        .split(|b| b == ',').collect::<Vec<&str>>();

    part2(lines)?;  // lol RIP part 1 code

    Ok(())
}