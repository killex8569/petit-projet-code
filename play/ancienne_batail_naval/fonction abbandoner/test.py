def display(self):
        # Affiche l'écran
        print("  " + " ".join(str(i) for i in range(self.cols)))
        for r in range(self.rows):
            print(f"{r} " + "|".join(self.grid[r]))  