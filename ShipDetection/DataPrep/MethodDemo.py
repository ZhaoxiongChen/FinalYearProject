import shutil
import os


class MethodDemo:

    def __init__(self, train_config, test_config, input_df, save_dir, side_length):
        self.train_config = train_config
        self.test_config = test_config
        self.input_df = input_df
        self.save_dir = save_dir
        self.target_size = (side_length, side_length)

    # Output augmented sample
    def output_aug_sample(self):
        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)
        op1 = self.train_config.flow_from_dataframe(
            dataframe=self.input_df,
            directory=os.path.dirname(self.input_df['Directory'].values[0]),
            x_col='Directory',
            y_col='HasShip',
            target_size=self.target_size,
            color_mode='rgb',
            class_mode='sparse',
            shuffle=False,
            batch_size=1,
            save_to_dir=self.save_dir,
            save_prefix='train_config_',
            save_format='jpg'
        )
        op1.next()
        op2 = self.test_config.flow_from_dataframe(
            dataframe=self.input_df,
            directory=os.path.dirname(self.input_df['Directory'].values[0]),
            x_col='Directory',
            y_col='HasShip',
            target_size=self.target_size,
            color_mode='rgb',
            class_mode='sparse',
            shuffle=False,
            batch_size=1,
            save_to_dir=self.save_dir,
            save_prefix='test_config_',
            save_format='jpg'
        )
        op2.next()
        shutil.copy(src=self.input_df['Directory'].values[0], dst=self.save_dir)
