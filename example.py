from anti_afk_lib.anti_afk import AntiAFK

def main():
    # Create an instance of AntiAFK with example parameters:
    # - run_duration: Run for 120 minutes
    anti_afk = AntiAFK(run_duration=120)
    
    # Run the anti-AFK simulation
    anti_afk.run()

if __name__ == '__main__':
    main()
