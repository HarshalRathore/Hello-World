function toggleForm(formType) {
    const phoneForm = document.getElementById('phoneForm');
    const emailForm = document.getElementById('emailForm');

    if (formType === 'phone') {
      phoneForm.style.display = 'flex';
      emailForm.style.display = 'none';
    } else if (formType === 'email') {
      phoneForm.style.display = 'none';
      emailForm.style.display = 'block';
    }
  }