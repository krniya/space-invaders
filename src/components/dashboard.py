"""
dashboard.py - Pygame Dashboard Module

This module defines a Pygame-based dashboard with a menu, providing an interactive user interface.
The dashboard allows users to navigate through menu options using mouse clicks or keyboard inputs.

Classes:
    - Dashboard: The main class representing the Pygame dashboard.

Enums:
    - MenuOption: Enum representing options in the dashboard menu.

Usage:
    To use this module, import the Dashboard class and MenuOption enum and create an instance
    of Dashboard to run the interactive dashboard.

"""

# pylint: disable=no-member, no-name-in-module

import sys
from typing import List, Optional, Tuple
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_UP, K_DOWN, K_RETURN
from components.enum import MenuOption


class Dashboard:
    """
    Dashboard Class - Pygame Interactive Dashboard

    This class represents an interactive dashboard in a Pygame environment.
    The dashboard includes a menu with options such as starting the game, viewing high scores, and quitting.

    Attributes:
        - screen (pygame.Surface): The Pygame surface to draw the dashboard on.
        - clock (pygame.time.Clock): Pygame clock for controlling the frame rate.
        - font (pygame.font.Font): Pygame font for rendering text.
        - menu_options (List[MenuOption]): List of available menu options.
        - selected_option (Optional[MenuOption]): Currently selected menu option.

    Methods:
        - handle_events(): Handle Pygame events such as mouse clicks and keyboard inputs.
        - handle_mouse_click(pos: Tuple[int, int]): Handle mouse click events based on the position.
        - move_selection(direction: int): Move the selected menu option up or down.
        - execute_selected_option(): Execute the action based on the selected menu option.
        - get_option_button(option: MenuOption) -> pygame.Rect: Get the rectangle for rendering the menu option.
        - draw_menu(): Draw the main menu on the screen.
        - run(): Run the main dashboard loop.

    Usage:
        To use this class, instantiate a Dashboard object with a Pygame surface,
        and then call the `run` method to start the interactive dashboard loop.

    """

    def __init__(self, screen: pygame.Surface):
        """Initialize the Dashboard

        Args:
            screen (pygame.Surface): The Pygame surface to draw the menu on.
        """
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("../assets/Font/monogram.ttf", 36)
        self.menu_options: List[MenuOption] = [
            MenuOption.PLAY,
            MenuOption.HIGH_SCORE,
            MenuOption.QUIT,
        ]
        self.selected_option: Optional[MenuOption] = None

    def handle_events(self):
        """Handle Pygame events."""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.handle_mouse_click(event.pos)
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    self.move_selection(-1)
                elif event.key == K_DOWN:
                    self.move_selection(1)
                elif event.key == K_RETURN:
                    self.execute_selected_option()

    def handle_mouse_click(self, pos: Tuple[int, int]):
        """Handle mouse click events.

        Args:
            pos (Tuple[int, int]): The mouse click position.
        """
        for option in self.menu_options:
            text_rect = self.get_option_button(option)
            if text_rect.collidepoint(pos):
                self.selected_option = option
                self.execute_selected_option()

    def move_selection(self, direction: int):
        """Move the selected option up or down.

        Args:
            direction (int): The direction to move (-1 for up, 1 for down).
        """
        if self.selected_option is not None:
            current_index = self.menu_options.index(self.selected_option)
            new_index = (current_index + direction) % len(self.menu_options)
            self.selected_option = self.menu_options[new_index]

    def execute_selected_option(self):
        """Execute the action based on the selected menu option."""
        if self.selected_option == MenuOption.PLAY:
            print("Starting the game!")
            # Add code to transition to the game screen
        elif self.selected_option == MenuOption.HIGH_SCORE:
            print("Viewing High Score")
            # Add code to display high scores
        elif self.selected_option == MenuOption.QUIT:
            pygame.quit()
            sys.exit()

    def get_option_button(self, option: MenuOption) -> pygame.Rect:
        """Get the rectangle for rendering the menu option.

        Args:
            option (MenuOption): The menu option.

        Returns:
            pygame.Rect: The rectangle for rendering the menu option.
        """
        text = self.font.render(option.name.replace("_", " "), True, (0, 0, 0))
        text_rect = text.get_rect(
            center=(
                self.screen.get_width() // 2,
                200 + self.menu_options.index(option) * 80,
            )
        )
        return text_rect

    def draw_menu(self):
        """Draw the main menu on the screen."""
        # * Setting screen caption
        clock = pygame.time.Clock()
        pygame.display.set_caption(
            f"Space Invaders running with {int(clock.get_fps())} FPS"
        )
        background = pygame.image.load("../assets/Graphics/background.png")
        menu_text = self.font.render("Space Inavders", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(background, (0, 0))
        self.screen.blit(menu_text, menu_rect)

        for option in self.menu_options:
            color = (255, 0, 0) if option == self.selected_option else (255, 255, 255)
            text = self.font.render(option.name.replace("_", " "), True, color)
            text_rect = self.get_option_button(option)
            self.screen.blit(text, text_rect)

    def run(self):
        """Run the main menu loop."""
        while True:
            self.handle_events()
            self.draw_menu()
            pygame.display.flip()
            self.clock.tick(30)
