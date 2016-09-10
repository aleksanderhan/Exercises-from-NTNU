namespace Client
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.searchButton = new System.Windows.Forms.Button();
            this.listAllButton = new System.Windows.Forms.Button();
            this.searchBox = new System.Windows.Forms.TextBox();
            this.listPersonsBox = new System.Windows.Forms.ListBox();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // searchButton
            // 
            this.searchButton.Location = new System.Drawing.Point(411, 48);
            this.searchButton.Name = "searchButton";
            this.searchButton.Size = new System.Drawing.Size(75, 23);
            this.searchButton.TabIndex = 0;
            this.searchButton.Text = "Search";
            this.searchButton.UseVisualStyleBackColor = true;
            this.searchButton.Click += new System.EventHandler(this.searchButton_Click);
            // 
            // listAllButton
            // 
            this.listAllButton.Location = new System.Drawing.Point(541, 188);
            this.listAllButton.Name = "listAllButton";
            this.listAllButton.Size = new System.Drawing.Size(75, 23);
            this.listAllButton.TabIndex = 1;
            this.listAllButton.Text = "List All";
            this.listAllButton.UseVisualStyleBackColor = true;
            this.listAllButton.Click += new System.EventHandler(this.listAllButton_Click);
            // 
            // searchBox
            // 
            this.searchBox.Location = new System.Drawing.Point(123, 70);
            this.searchBox.Name = "searchBox";
            this.searchBox.Size = new System.Drawing.Size(100, 20);
            this.searchBox.TabIndex = 2;
            this.searchBox.TextChanged += new System.EventHandler(this.searchBox_TextChanged);
            // 
            // listPersonsBox
            // 
            this.listPersonsBox.FormattingEnabled = true;
            this.listPersonsBox.Location = new System.Drawing.Point(204, 110);
            this.listPersonsBox.Name = "listPersonsBox";
            this.listPersonsBox.Size = new System.Drawing.Size(227, 264);
            this.listPersonsBox.TabIndex = 3;
            this.listPersonsBox.SelectedIndexChanged += new System.EventHandler(this.listPersonsBox_SelectedIndexChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(62, 58);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(44, 13);
            this.label1.TabIndex = 4;
            this.label1.Text = "Search:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(765, 392);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.listPersonsBox);
            this.Controls.Add(this.searchBox);
            this.Controls.Add(this.listAllButton);
            this.Controls.Add(this.searchButton);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button searchButton;
        private System.Windows.Forms.Button listAllButton;
        private System.Windows.Forms.TextBox searchBox;
        private System.Windows.Forms.ListBox listPersonsBox;
        private System.Windows.Forms.Label label1;
    }
}

