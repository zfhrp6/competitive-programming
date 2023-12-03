use proconio::input;

struct Clock {
    hour: isize,
    minute: isize,
    second: isize,
}

impl Clock {
    pub fn set(&mut self, h: isize, m: isize, s: isize) {
        self.hour = h;
        self.minute = m;
        self.second = s;
    }

    pub fn to_string(&self) -> String {
        return format!("{:02}:{:02}:{:02}", self.hour, self.minute, self.second);
    }

    pub fn shift(&mut self, dif: isize) {
        let h_dif = dif / 3600;
        let m_dif = (dif % 3600) / 60;
        let s_dif = dif % 60;
        self.hour += h_dif;
        self.minute += m_dif;
        self.second += s_dif;
        self.carry();
    }

    fn carry(&mut self) {
        self.carry_down();
        self.carry_up();
    }

    fn carry_up(&mut self) {
        if self.second >= 60 {
            self.minute += 1;
            self.second -= 60;
        }
        if self.minute >= 60 {
            self.hour += 1;
            self.minute -= 60;
        }
        if self.hour >= 24 {
            self.hour -= 24
        }
    }

    fn carry_down(&mut self) {
        if self.second < 0 {
            self.minute -= 1;
            self.second += 60;
        }
        if self.minute < 0 {
            self.hour -= 1;
            self.minute += 60;
        }
        if self.hour < 0 {
            self.hour += 24;
        }
    }
}

fn main() {
    input! {
        h: isize,
        m: isize,
        s:isize,
        diff:isize,
    }

    let mut c = Clock {
        hour: h,
        minute: m,
        second: s,
    };
    println!("{}", c.to_string());
    c.shift(diff);
    println!("{}", c.to_string());
}
