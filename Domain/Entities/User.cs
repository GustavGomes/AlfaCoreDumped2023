using System.ComponentModel.DataAnnotations;

namespace AlfaCoreDumped.Domain.Entities
{
    public class User
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        public string UserName { get; set; }

        [Required]
        public string Password { get; set; }

        [Required]
        public string Cpf { get; set; }

        [Required]
        public string RoleName { get; set; }

        [Required]
        public string RoleId { get; set; }

        [Required]
        public string Cbo { get; set; }

        public ICollection<string> Permissions { get; set; }
            = new List<string>();

        public ICollection<Solicitation> Solicitations { get; set; }
            = new List<Solicitation>();
    }
}
