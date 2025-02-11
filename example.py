from anti_afk.anti_afk import AntiAFK

def main():
    # Create an instance of AntiAFK with example parameters:
    # - run_duration: Run for 120 minutes
    anti_afk = AntiAFK(run_duration=120, log_actions=True)
    
    # Run the anti-AFK simulation
    anti_afk.run()

if __name__ == '__main__':
    main()
