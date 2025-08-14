Public Class Form1

    Private Sub btnShow_Click(sender As System.Object, e As System.EventArgs) Handles btnShow.Click
        ' Get values from textboxes
        Dim name As String = txtName.Text.Trim()
        Dim acType As String = txtType.Text.Trim()
        Dim hp As String = txtHP.Text.Trim()

        ' Validation
        If name = "" Or acType = "" Or hp = "" Then
            MessageBox.Show("Please fill in all fields.", "Validation", MessageBoxButtons.OK, MessageBoxIcon.Warning)
            Exit Sub
        End If

        If Not IsNumeric(hp) Then
            MessageBox.Show("Horse Power must be a number.", "Validation", MessageBoxButtons.OK, MessageBoxIcon.Warning)
            Exit Sub
        End If

        ' Show details
        Dim details As String = "Aircon Name: " & name & vbCrLf &
                                "Aircon Type: " & acType & vbCrLf &
                                "Horse Power: " & hp & " HP"

        MessageBox.Show(details, "Aircon Details", MessageBoxButtons.OK, MessageBoxIcon.Information)
    End Sub

End Class
